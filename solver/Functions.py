import numpy as np


def gauss_I(X, x0, A, D, T):
    """
    Gaussian pulse

    :param X: time (input)
    :param x0: time shift of a pulse
    :param A: pulse amplitude
    :param D: pulse width
    :param T: pulses period
    :return: output current
    """
    k = np.fix(X / T)
    if k == 0:
        return A * np.exp(-(X - x0) ** 2 / (2 * D)) + A * np.exp(-(X - x0 - T) ** 2 / (2 * D))
    else:
        return A * np.exp(-(X - x0 - T * (k - 1)) ** 2 / (2 * D)) + A * np.exp(-(X - x0 - T * k) ** 2 / (2 * D)) \
               + A * np.exp(-(X - x0 - T * (k + 1)) ** 2 / (2 * D))


def pulse_I(t, t0, length, A):
    """
    Rectangular pulse from t0 to t0+length

    :param t: time (input)
    :param t0: pulse start time
    :param length: pulse length
    :param A: pulse amplitude (in normalized current units)
    :return: output current
    """
    return 0 if t <= t0 or t >= t0 + length else A


def pulses_I(t, t01, t02, length, A):
    return A if (t01 <= t <= t01 + length) or (t02 <= t <= t02 + length) else 0


def sin_I(t, t0, length, w, A):
    """
    Sinusoidal current from t0 to t0+length

    :param t: time (input)
    :param t0: current start time
    :param length: current length
    :param w: pulse frequency (omega)
    :param A: pulse amplitude (in normalized current units)
    :return: output current
    """
    if t <= t0 or t >= t0 + length:
        return 0
    else:
        return A * np.sin(w * (t - t0))


def periodic_square(t, t0, pulse_length, total_length, freq, A):
    if t < t0 or t >= t0 + total_length:
        return 0
    else:
        period = 1 / freq
        abs_time = t - t0
        n_periods_before = np.fix(abs_time / period)
        corrected_time = abs_time - period * n_periods_before
        return A if corrected_time <= pulse_length else 0