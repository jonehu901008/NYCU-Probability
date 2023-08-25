def problem2_b(simulation_times, pos):
    x = np.random.uniform(-1, 1, simulation_times)
    y = np.random.uniform(-1, 1, simulation_times)
    res = (x - 0.2)**2 + 2*(y + 0.3)**2
    ins = res <= 0.25
    Ans = ins.sum()/simulation_times

    plt.subplot(2, 2, pos)
    
    plt.scatter(x[ins], y[ins], color = 'red')
    plt.scatter(x[~ins], y[~ins], color = 'black')
    

    plt.legend(loc = 'upper right')
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    n = str(simulation_times).count('0')
    plt.title('n = 10^' + str(n) ', Area = ' + str(Ans))
    return Ans

fig = plt.figure(figsize = (8, 8), dpi = 110)
for i,j in zip(range(1,9,2), range(1,5)):
  ans = problem2_b(10**i, j)

plt.tight_layout()