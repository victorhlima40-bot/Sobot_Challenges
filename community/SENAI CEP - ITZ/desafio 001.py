import serial
from time import sleep

# Configuração da porta serial
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()     # Aguarda a configuração dos dados

# Habilita os motores das rodas
usb.write(b"MT0 E1")
sleep(0.1)

# --- SEQUÊNCIA DE COMANDOS (1 a 11) ---

# 1. Forward, Green
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D1000 AT5000 DT5000 V10")
sleep(6.0) # Tempo estimado para concluir o movimento

# 2. Left, Blue
usb.write(b"LT E1 RD0 GR0 BL50")
usb.write(b"MT0 E1 D90 L AT3950 DT3950 V10")
sleep(4.0)

# 3. Forward, Green
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D1000 AT5000 DT5000 V10")
sleep(6.0)

# 4. Right, Yellow
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(4.0)

# 5. Forward, Green
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D1000 AT5000 DT5000 V10")
sleep(6.0)

# 6. Backward, Red
usb.write(b"LT E1 RD50 GR0 BL0")
usb.write(b"MT0 E1 D-1000 AT5000 DT5000 V10") # Distância negativa para ré
sleep(6.0)

# 7. Right, Yellow
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(4.0)

# 8. Forward, Green
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D1000 AT5000 DT5000 V10")
sleep(6.0)

# 9. Right, Yellow
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(4.0)

# 10. Forward, Green
usb.write(b"LT E1 RD0 GR50 BL0")
usb.write(b"MT0 E1 D1000 AT5000 DT5000 V10")
sleep(6.0)

# 11. Right, Yellow
usb.write(b"LT E1 RD50 GR50 BL0")
usb.write(b"MT0 E1 D90 R AT3950 DT3950 V10")
sleep(4.0)

# --- ENCERRAMENTO ---
usb.write(b"LT E1 RD0 GR0 BL0")    # Desliga a fita de LED
usb.write(b"MT0 E1 D0 AT0 DT0 V0") # Para o robô completamente
usb.write(b"MT0 E0")                # Desativa os motores das rodas
