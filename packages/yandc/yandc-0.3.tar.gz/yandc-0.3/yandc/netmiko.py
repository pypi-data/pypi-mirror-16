from yandc_cumulus import Client as CL_Client
from yandc_eos import Client as EOS_Client
from yandc_ios import Client as IOS_Client
from yandc_iosxr import Client as XR_Client
from yandc_ros import Client as ROS_Client


class ConnectHandler(object):
    def __del__(self):
        self.disconnect()

#   def __init__(self, ip, username, password, secret='', port=22, device_type='', verbose=True):
    def __init__(self, *args, **kwargs):
        client_kwargs = {}

        if 'host' in kwargs:
            client_kwargs['host'] = kwargs['host']
        elif 'ip' in kwargs:
            client_kwargs['host'] = kwargs['ip']
        else:
            raise ValueError('No Host or IP specified')

        if 'username' in kwargs:
            client_kwargs['username'] = kwargs['username']
        if 'password' in kwargs:
            client_kwargs['password'] = kwargs['password']
        if 'port' in kwargs:
            client_kwargs['ssh_port'] = kwargs['port']
        print client_kwargs

        if kwargs['device_type'] == 'arista_eos':
            self.yandc_client = EOS_Client(**client_kwargs)
        elif kwargs['device_type'] == 'cisco_ios':
            self.yandc_client = IOS_Client(**client_kwargs)
        elif kwargs['device_type'] == 'cisco_xr':
            self.yandc_client = XR_Client(**client_kwargs)
        elif kwargs['device_type'] == 'cumulus_linux':
            self.yandc_client = CL_Client(**client_kwargs)
        elif kwargs['device_type'] == 'mikrotik':
            self.yandc_client = ROS_Client(**client_kwargs)
        else:
            raise ValueError('Device type ' + kwargs['device_type'] + ' not supported')

    def check_config_mode(self):
        return self.yandc_client.in_configure_mode()

    def cleanup(self):
        pass

    def clear_buffer(self):
        pass

    def config_mode(self, config_command='', *args):
        return NotImplementedError

    def disconnect(self):
        if hasattr(self, 'yandc_client'):
            self.yandc_client.disconnect()
            del self.yandc_client

    def enable(self):
        return ''

    def establish_connection(self, sleep_time=3, verbose=True):
        pass

    def disable_paging(self):
        pass

    def exit_config_mode(self, exit_config, *args):
        return NotImplementedError

    def find_prompt(self):
        return self.yandc_client.ssh_shell.last_prompt

#   def send_command(self, command_string, delay_factor=1, max_loops=30):
    def send_command(self, command_string, *args):
        return unicode('\n'.join(self.yandc_client.cli_command(command_string)))

    def send_config_from_file(self, config_file, **kwargs):
        with open(config_file, 'rU') as f:
            self.send_config_set(f.read().splitlines())

    def send_config_set(self, config_commands):
        return self.yandc_client.configure_via_cli(config_commands)

    def strip_prompt(self, a_string):
        pass

    def strip_command(self, command_string, output):
        pass

    def normalize_linefeeds(self, a_string):
        pass
