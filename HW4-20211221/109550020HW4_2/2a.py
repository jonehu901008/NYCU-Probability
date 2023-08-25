# 10^3 20次
Test1 = []
for i in range(20):
    z = np.random.normal(0, 1, 1000)
    y = (np.cos(z) + np.sin(2*z))
    Test1.append(y.mean())

Test2 = []
for i in range(20):
    z = np.random.normal(0, 1, 100000)
    y = (np.cos(z) + np.sin(2*z))
    Test2.append(y.mean())

fig = plt.figure(figsize = (10, 3), dpi = 110)
plt.plot(Test1, label = 'n = 10^3, 20 times, E(Y) = ' + str((sum(Test1)/len(Test1)).round(4)))
plt.plot(Test2, color = 'orange', label = f'n = 10^5, 20 times, E(Y) = {(sum(Test2)/len(Test2)).round(4)}')
plt.xticks(np.arange(20))
plt.legend()
plt.title('Problem 2(a)')