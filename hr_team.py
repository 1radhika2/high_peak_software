if __name__=="__main__":
	x = open("sample_input.txt", "r")
	# read_content = x.readline()
	read_content = 1
	read_content = x.readline()
	emp_num = read_content.split(':')
	emp_num = emp_num[-1].strip()
	emp_num = int(emp_num)
	dcnry = {}
	read_content = x.readline()
	read_content = x.readline()
	read_content = x.readline()
	while(read_content):
		read_content = x.readline()
		goodie_var = read_content.split(':')
		if(len(goodie_var[0])==0 or len(goodie_var[1])==0):
			continue
		goodie_company = goodie_var[-1].strip()
		goodie_company = int(goodie_company)
		goodie_size = goodie_var[0].strip()
		dcnry[goodie_size] = goodie_company
	di_sort = dict(sorted(dcnry.items(), key=lambda item: (item[1])))
	new_list = list(di_sort)
	wri = open("sample_output.txt", "w")
	wri.write("The goodies selected for distribution are:\n\n")
	for i in range(emp_num):
		out_str = new_list[i] + ": " + str(di_sort[new_list[i]])
		wri.write(out_str + "\n")
	val = di_sort[new_list[emp_num -1]] - di_sort[new_list[0]]
	wri.write("\nAnd the difference between the chosen goodie with highest price and the lowest price is " + str(val) + "\n")
	wri.close()
	x.close()
