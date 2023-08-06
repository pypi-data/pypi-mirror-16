from jsonrpc import dispatcher
from .rpc import RpcClient, RpcServer

import multiprocessing
import traceback

class MAPI():
    def __init__(self, module):
        self.mod = module

    def InvokeCommand(self, cmd_data):
        try:
            command = self.mod.commands[cmd_data["Name"]]
            command.get("Fun")(cmd_data["Msg"], cmd_data["Args"])
        except:
            traceback.print_exc()
            raise
        return ""

    def Cleanup(self, clean_data):
        if clean_data:
            # Nothing to handle yet
            return ""
        return ""

class Module:
    def __init__(self, name, desc):
        self.master = None
        self.name = name
        self.desc = desc
        self.commands = dict()
        self.lock = multiprocessing.Lock()
        self.port = 0
        self.rpc_server = RpcServer()

    def create_rpc_server(self):
        mapi = MAPI(self)
        dispatcher.build_method_map(mapi, self.name+".")
        self.port = self.rpc_server.get_sock_port()

    def command(self, name):
        def add(command):
            self.commands[name] = {"Fun": command}
        return add

    def add_command(self, name, command):
        self.commands[name] = command
    
    def register_command(self, name):
        data = dict(CommandName=name, ModuleName=self.name)
        self.master.call("Master.RegisterCommand", data)

    def register(self, args):
        self.master = RpcClient(args[1])
        self.create_rpc_server()
        for name, _ in self.commands.items():
            self.register_command(name)
        self.master.call("Master.Register", dict(Port=str(self.port), ModuleName=self.name))
        self.rpc_server.start_serving()

    def say(self, channel, text):
        self.master.call("Master.Send", channel + " :" + text)
