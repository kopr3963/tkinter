import commands;
from itertools import izip;

# os check flag add
st = command = commands.getstatusoutput('v4l2-ctl -d /dev/video0 --list-ctrls');
st = st[1];
st = st.strip();
st = st.replace(" ","");
out = st.split("\n");

def list_to_dict(list):
	s = []; 
	for i in range(len(list)):
		s = s + list[i].split(":");
	i = iter(s);
	result = dict(izip(i,i));
	return result;
result  = list_to_dict(out);
print ( result.keys());
print ( result.values());

