# encoding:utf-8
formula = {
    u"浙江": {
        0: lambda x, t: 0.09 * x * t,
        15: lambda x, t: (0.12 - 0.002 * t) * x * t,
        30: lambda x, t: 0.06 * x * t,
    },
    u"上海": {
      0: lambda x, t: 0.6 * x,
      2: lambda x, t: 0.9 * x,
      5: lambda x, t: 1.02 * x,
      10: lambda x, t: 1.315 * x,
      15: lambda x, t: 1.428 * x,
    },
    u"江苏": {
        0: lambda x, t: 0.09 * x * t,
        10: lambda x, t: (8 / 75 - t / 600) * x * t,
        40: lambda x, t: 0.04 * x * t,
    },
    u"安徽": {
        0: lambda x, t: 0.09 * x * t,
        10: lambda x, t: (31 / 300 - t / 750) * x * t,
        40: lambda x, t: 0.05 * x * t,
    },
    u"江西": {
        0: lambda x, t: 0.09 * x * t,
        10: lambda x, t: (0.105 - 0.0015 * t) * x * t,
        40: lambda x, t: 0.045 * x * t,
    },
}
