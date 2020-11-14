def obvod_v_mm(r):
    PI = 3.14
    M2MM = 1000
    return 2*PI*r*M2MM

def obvod_v_mm2(r):
    return 6280.0*r



print(obvod_v_mm(3))
print(obvod_v_mm2(3))