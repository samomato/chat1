# 寫讀取成list的function
def read_file(filename):
	chat = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			chat.append(line.strip())
	return chat


# 寫變更成output格式的function
def change_format(name1, name2, chat):
	new_chat = []
	last_name = None
	for line in chat:
		if name1 == line:
			last_name = name1
			continue
		elif name2 == line:
			last_name = name2
			continue
		
		if last_name:
			new_chat.append(last_name + ': ' + line)
	return new_chat

# 輸出成新的txt
def write_file(filename, new_chat):
	with open(filename, 'w', encoding = 'utf-8') as f:
		for line in new_chat:
			f.write(line + '\n')


# 寫出main function
def main():
	new_chat = change_format('Allen', 'Tom', read_file('input.txt'))
	write_file('output_Reeve.txt', new_chat)

# 執行main function
main()