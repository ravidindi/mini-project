import pickle as pickle
with open('a.pkl', 'rb') as handle:
    b1 = pickle.load(handle)
# with open('assault.pkl', 'rb') as handle1:
#     b2 = pickle.load(handle1)
# with open('data_1.pkl', 'rb') as handle3:
#     b3 = pickle.load(handle3)
# l=[]
# for i in range(len(b1)):
#     l.append(b1[i])
# for i in range(len(b2)):
#     l.append(b2[i])
# for i in range(len(b3)):
#     l.append(b3[i])
# print(len(b1))
# print(len(b2))
# print(len(b3))
print(b1)

# with open('dataf.pkl', 'wb') as handle:
#     pickle.dump(l, handle, protocol=pickle.HIGHEST_PROTOCOL)