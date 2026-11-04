data = {"banana":3,"apple":2,"cherry":4}
asen = dict(sorted (data.items()))
print("ascending order in key",asen)
desen = dict(sorted (data.items(),reverse = True))
print("descending order in key",desen)
