# Positive Reinforcement for Long-Term Fairness

This is the repository associated with the paper "A Dynamic Decision-Making Framework Promoting Long-Term Fairness", AIES 2022. A part of this work has also been presented at ICML RDMDE 2022 and ICLR SRML 2022. 

As AI-based decision-making becomes increasingly impactful on human society, the study of the influence of fairness-aware policies on the population becomes important. In this work, we propose a framework for sequential decision-making aimed at dynamically influencing long-term societal fairness, illustrated via the problem of selecting applicants from a pool consisting of two groups, one of which is under-represented. We consider a dynamic model for the composition of the applicant pool, where the admission of more applicants from a particular group positively reinforces more such candidates to participate in the selection process. Under such a model, we show the efficacy of the proposed Fair-Greedy selection policy which systematically trades greedy score maximization against fairness objectives. In addition to experimenting on synthetic data, we adapt static real-world datasets on law school candidates and credit lending to simulate the dynamics of the composition of the applicant pool.

Dependencies: numpy, scipy, scikit-learn, aif360, gerryfair

If you have any questions regarding the code, please contact bpuranik[at]ucsb[dot]edu

If you found this repo useful, please consider citing our work:
Bhagyashree Puranik, Upamanyu Madhow, and Ramtin Pedarsani. 2022. A Dynamic Decision-Making Framework Promoting Long-Term Fairness. In Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society (AIES '22). Association for Computing Machinery, New York, NY, USA, 547–556. https://doi.org/10.1145/3514094.3534127

