class SingleStateKalmanFilter(object):

    def __init__(self, A, B, C, x, P, Q, R):
        self.A = A
        self.B = B
        self.C = C
        self.current_state_estimate = x
        self.current_prob_estimate = P
        self.Q = Q
        self.R = R

    def current_state(self):
        return self.current_state_estimate

    def step(self, control_input, measurement):
        predicted_state_estimate = self.A * self.current_state_estimate + self.B * control_input
        predicted_prob_estimate = self.A * self.current_prob_estimate * self.A + self.Q
        innovation = measurement - self.C * predicted_state_estimate
        innovation_covariance = self.C * predicted_prob_estimate * self.C + self.R
        kalman_gain = predicted_prob_estimate * self.C * 1 / float(innovation_covariance)
        self.current_state_estimate = predicted_state_estimate + kalman_gain * innovation
        self.current_prob_estimate = (1 - kalman_gain * self.C) * predicted_prob_estimate
