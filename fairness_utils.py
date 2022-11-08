import numpy as np
from scipy.stats import norm


def gaussian_expected_top_r_of_n(r, n, mu, sigma):
    if r<1:
        return 0
    
    method = 'approx' # Choose 'approx' or 'monte-carlo'
    
    if method == 'monte-carlo':
        Nsamples = 1000
        val = 0
        for i in range(Nsamples):
            scores = mu + sigma*np.random.randn(n,1)
            sorted_scores = np.sort(scores.flatten())
            sorted_scores = sorted_scores[::-1]
            val = val + sorted_scores[r-1]
        val = val/Nsamples
    
    elif method == 'approx':
        alpha = 0.375
        p = (r - alpha)/(n-2*alpha+1)
        val = -norm.ppf(p)
        val = sigma*val+mu
    
    return val

def get_greedy_reward(dist_type, mean_u, std_u, mean_v, std_v, N, a_bar, st):
    Nu = round(N*st)
    Nv = N - Nu
    A = a_bar*N
    actions = np.arange(A+1)/A

    greedy_reward = np.zeros(len(actions))

    for i in range(int(A+1)):
        at = actions[i]
        Au = min(at*A, Nu)
        Av = A - Au

        if Av>Nv:
            Av = Nv
            Au = A - Av

        reward_u = 0
        reward_v = 0

        for j in range(int(Au)):
            reward_u = reward_u + gaussian_expected_top_r_of_n(j+1, Nu, mean_u, std_u)

        for j in range(int(Av)):
            reward_v = reward_v + gaussian_expected_top_r_of_n(j+1, Nv, mean_v, std_v)

        greedy_reward[i] = (1/A)*(reward_u + reward_v)
        
    return greedy_reward

def process_evolution(theta_init, lambda_, eta, N, a_bar, s_bar, greedy_reward_table, num_rounds = 200):
    theta = theta_init 

    applicants_u = np.zeros(num_rounds)
    admitted_u = np.zeros(num_rounds)
    theta_vec = np.zeros(num_rounds+1)
    theta_vec[0] = theta
    overall_utility_fg_policy = np.zeros(num_rounds)

    for k in range(num_rounds):
        Nu_ = min(N, np.random.poisson(theta*N))
        A = a_bar*N
        actions = np.arange(A+1)/A
        overall_reward = greedy_reward_table[Nu_,:] - lambda_*np.square(actions - s_bar)
        overall_utility_fg_policy[k] = np.max(overall_reward)
        optimal_action_idx = np.argmax(overall_reward)
        optimal_action = actions[optimal_action_idx]

        # Applicant pool evolution:
        theta = min(max(0, theta+eta*(optimal_action - Nu_/N)),1)
        #print(Nu_, N, theta, optimal_action)
        applicants_u[k] = Nu_/N
        admitted_u[k] = optimal_action
        theta_vec[k+1] = theta
    return applicants_u, admitted_u, theta_vec, overall_utility_fg_policy
