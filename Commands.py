commands = []


def registered_command(command):
    """Binds command to the global command set"""
    command_name = '-'.join(command.__name__.split('_')[:-1])
    print(f'Registering bot command: {command_name}')
    commands.append({'name': command_name,
                     'action': command})

    return command


@registered_command
def start_command(update, context):
    update.message.reply_text('Type something')


@registered_command
def help_command(update, context):
    update.message.reply_text('If you need help, ask!')


def add_command_handlers(registry_add):
    """Accessor to all locally defined commands


       Parameters:
       registry_add: delegate accepting a command as {:name, :action}
       """
    for command in commands:
        registry_add(command)
