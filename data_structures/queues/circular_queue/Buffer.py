from circular_queue import CircularQueue
import numpy as np
import cv2

class VideoBuffer:
    def __init__(self, buffer_size: int, frame_width: int = 256, frame_height: int = 256):
        self.buffer = CircularQueue(buffer_size)
        self.frame_width = frame_width
        self.frame_height = frame_height

    def generate_frame(self) -> np.ndarray:
        """Genera un frame en blanco y negro de 256x256 píxeles."""
        return np.random.randint(0, 2, (self.frame_height, self.frame_width), dtype=np.uint8) * 255

    def fill_buffer(self):
        """Llena el buffer con frames generados automáticamente."""
        for _ in range(self.buffer.max):
            frame = self.generate_frame()
            self.buffer.enqueue(frame)

    def display_frames(self):
        """Muestra los frames uno por uno, permitiendo al usuario avanzar manualmente."""
        while True:
            frame = self.buffer.dequeue()
            if frame is None:
                print("Buffer vacío. Saliendo...")
                break

            cv2.imshow("Video Buffer", frame)
            key = cv2.waitKey(0)  # Espera a que el usuario presione una tecla

            if key == ord('q'):  # Presiona 'q' para salir
                break

        cv2.destroyAllWindows()


# Uso del código
if __name__ == "__main__":
    # Crear un buffer de vídeo con capacidad para 30 frames
    video_buffer = VideoBuffer(buffer_size=30)

    # Llenar el buffer con frames generados automáticamente
    video_buffer.fill_buffer()

    # Mostrar los frames uno por uno
    video_buffer.display_frames()