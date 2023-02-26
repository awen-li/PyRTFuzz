import re

def api_info_parser(api_header: str) -> str:
    start = api_header.index(']') + 1
    info = api_header[start:].strip()
    if info == '-':
        return None
    return info

def main():
    path = './unrecognized_api_spec.txt'
    tmp_path = './unrecognized_api_writeline.txt'
    
    wls = []
    with open(path, 'r') as f:
        for api in f.readlines():
            args_pattern = "--\sArgs:\[.*\],"
            args = re.search(args_pattern, api).group(0)[8:-1]
            api_info = re.split(args_pattern, api)[0].split(',')
            api_header = ''
            for i in api_info:
                tmp = api_info_parser(i)
                if tmp != None:
                    api_header += tmp + '.'
                    
            wl = "self.AddHdcApi (" + api_header + "', " + args + ")\n"
            wls.append(wl)        
    f.close()
    
    with open(tmp_path, 'w') as output:
        output.writelines(wls)
    output.close()

if __name__ == '__main__': 
    main()