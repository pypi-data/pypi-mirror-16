from queue import Queue
from threading import Thread

from ipykernel.kernelbase import Kernel
import subprocess
import tempfile
import os
import os.path as path

class RealTimeSubprocess(subprocess.Popen):
    """
    A subprocess that allows to read its stdout and stderr in real time
    """

    def __init__(self, cmd, write_to_stdout, write_to_stderr):
        """
        :param cmd: the command to execute
        :param write_to_stdout: a callable that will be called with chunks of data from stdout
        :param write_to_stderr: a callable that will be called with chunks of data from stderr
        """
        #fsa = open('C:\\Users\\silvio\\Documents\\Dev\\nim\\jupyter-nim-kernel\\tt.txt','a')
        #fsa.write(str(cmd))

        self._write_to_stdout = write_to_stdout
        self._write_to_stderr = write_to_stderr

        super().__init__(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=0)

        self._stdout_queue = Queue()
        self._stdout_thread = Thread(target=RealTimeSubprocess._enqueue_output, args=(self.stdout, self._stdout_queue))
        self._stdout_thread.daemon = True
        self._stdout_thread.start()

        self._stderr_queue = Queue()
        self._stderr_thread = Thread(target=RealTimeSubprocess._enqueue_output, args=(self.stderr, self._stderr_queue))
        self._stderr_thread.daemon = True
        self._stderr_thread.start()

    @staticmethod
    def _enqueue_output(stream, queue):
        """
        Add chunks of data from a stream to a queue until the stream is empty.
        """
        for line in iter(lambda: stream.read(4096), b''):
            queue.put(line)
        stream.close()

    def write_contents(self):
        """
        Write the available content from stdin and stderr where specified when the instance was created
        :return:
        """

        def read_all_from_queue(queue):
            res = b''
            size = queue.qsize()
            while size != 0:
                res += queue.get_nowait()
                size -= 1
            return res

        stdout_contents = read_all_from_queue(self._stdout_queue)
        if stdout_contents:
            self._write_to_stdout(stdout_contents)
        stderr_contents = read_all_from_queue(self._stderr_queue)
        if stderr_contents:
            self._write_to_stderr(stderr_contents)

class MyRandomSequence(tempfile._RandomNameSequence):
    characters = "abcdefghijklmnopqrstuvwxyz0123456789"

class NimKernel(Kernel):
    implementation = 'jupyter_nim_kernel'
    implementation_version = '1.0'
    language = 'nim'
    language_version = '0.14.2'
    language_info = {'name': 'nim',
                     'mimetype': 'text/plain',
                     'file_extension': 'nim'}
    banner = "Nim kernel.\n" \
             "Uses nim, and creates source code files and executables in temporary folder.\n"

    def __init__(self, *args, **kwargs):
        super(NimKernel, self).__init__(*args, **kwargs)
        self.files = []
      # mastertemp = tempfile.mkstemp(suffix='.out')
      # os.close(mastertemp[0])
      # self.master_path = mastertemp[1] # absolute pathname to tmpfile
      # msp = "-o:"+self.master_path
      # filepath = path.join(path.dirname(path.realpath(__file__)), '..', 'resources', 'master.nim')
      # subprocess.call(['nim', 'c', '--verbosity:0', '--app:lib', msp, filepath])
      # subprocess.call(['gcc', filepath, '-std=c11', '-rdynamic', '-ldl', '-o', self.master_path])

    def cleanup_files(self):
        """Remove all the temporary files created by the kernel"""
        for file in self.files:
            os.remove(file)
        #os.remove(self.master_path)

    def new_temp_file(self, **kwargs):
        """Create a new temp file to be deleted when the kernel shuts down"""
        # We don't want the file to be deleted when closed, but only when the kernel stops
        kwargs['delete'] = False
        kwargs['mode'] = 'w'
        kwargs['prefix'] = 'nim'

        # only names which are ok for nim modules
        tempfile._name_sequence = MyRandomSequence()

        file = tempfile.NamedTemporaryFile(**kwargs)
        self.files.append(file.name)
        return file

    def _write_to_stdout(self, contents):
        self.send_response(self.iopub_socket, 'stream', {'name': 'stdout', 'text': contents})

    def _write_to_stderr(self, contents):
        self.send_response(self.iopub_socket, 'stream', {'name': 'stderr', 'text': contents})

    def create_jupyter_subprocess(self, cmd):
        return RealTimeSubprocess(cmd,
                                  lambda contents: self._write_to_stdout(contents.decode()),
                                  lambda contents: self._write_to_stderr(contents.decode()))

    def compile_with_nimc(self, source_filename, binary_filename):
        #args = ['gcc', source_filename, '-std=c11', '-fPIC', '-shared', '-rdynamic', '-o', binary_filename]
        obf = '-o:'+binary_filename
        args = ['nim', 'c', '--hint[Processing]:off', '--verbosity:0', '-t:-fPIC', '-t:-shared', obf, source_filename]
        return self.create_jupyter_subprocess(args)

    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        with self.new_temp_file(suffix='.nim') as source_file:
            source_file.write(code)
            source_file.flush()
            with self.new_temp_file(suffix='.out') as binary_file:
                p = self.compile_with_nimc(source_file.name, binary_file.name)
                while p.poll() is None:
                    p.write_contents()
                p.write_contents()
                if p.returncode != 0:  # Compilation failed
                    self._write_to_stderr(
                            "[Nim kernel] nimc exited with code {}, the executable will not be executed".format(
                                    p.returncode))
                    return {'status': 'ok', 'execution_count': self.execution_count, 'payload': [],
                            'user_expressions': {}}

        p = self.create_jupyter_subprocess([binary_file.name]) #self.master_path,
        while p.poll() is None:
            p.write_contents()
        p.write_contents()

        if p.returncode != 0:
            self._write_to_stderr("[Nim kernel] Executable exited with code {}".format(p.returncode))
        return {'status': 'ok', 'execution_count': self.execution_count, 'payload': [], 'user_expressions': {}}

    def do_shutdown(self, restart):
        """Cleanup the created source code files and executables when shutting down the kernel"""
        self.cleanup_files()

    def do_complete(self, code, cursor_pos):
        ws = set('\n\r\t ')
        lf = set('\n\r')
        sw = cursor_pos
        while sw > 0 and code[sw - 1] not in ws:
            sw -= 1
        sl = sw
        while sl > 0 and code[sl - 1] not in lf:
            sl -= 1
        wrd = code[sw:cursor_pos]
#        lin = code[sl:cursor_pos]
        # TODO: nimsuggest??
        r = 'addr and as asm atomic bind block break case cast concept ' \
            'const continue converter defer discard distinct div do ' \
            'elif else end enum except export finally for from func ' \
            'generic if import in include interface is isnot iterator ' \
            'let macro method mixin mod nil not notin object of or out ' \
            'proc ptr raise ref return shl shr static template try ' \
            'tuple type using var when while with without xor yield'.split()
        return {'status': 'ok', 'matches': [t for t in r if t.startswith(wrd)],
                'cursor_start': sw, 'cursor_end': cursor_pos, 'metadata': {}}