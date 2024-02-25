chat_logs = []

def command_chat(chat_commands, chat_logs):
    chat_logs.append(chat_commands)

def command_delete(command, chat_logs):
    if command in chat_logs:
        chat_logs.remove(command)

def command_edit(command, edit, chat_logs):
    if command in chat_logs:
        index = chat_logs.index(command)
        chat_logs[index] = edit

def command_pin(command, chat_logs):
    if command in chat_logs:
        chat_logs.remove(command)
        chat_logs.append(command)

def command_spam(chat_commands, chat_logs):
    chat_logs.extend(chat_commands)

def print_chat(chat_logs):
    for command in chat_logs:
        print(command)

while True:
    command = input().split()
    action = command[0]

    if action == 'Chat':
        command_chat(command[1], chat_logs)
    elif action == 'Delete':
        command_delete(command[1], chat_logs)
    elif action == 'Edit':
        command_edit(command[1], command[2], chat_logs)
    elif action == 'Pin':
        command_pin(command[1], chat_logs)
    elif action == 'Spam':
        command_spam(command[1:], chat_logs)
    elif action == 'end':
        break

print_chat(chat_logs)
