import os
import matplotlib.pyplot as plt
import moviepy.video.io.ImageSequenceClip

def plot_simulation(particles, frame_number):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_ylim([-50,50])
    ax.set_xlim([-50,50])
    for particle in particles:
        x, y = particle.position
        ax.scatter(x, y, s= abs(particle.mass) * 5)

    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('Particle Simulation')
    plt.savefig(f'images\\frame_{frame_number:04d}.png')
    plt.close()

def write_to_video():
    image_folder='images'
    fps=10
    image_files = [os.path.join(image_folder,img)
               for img in os.listdir(image_folder)
               if img.endswith(".png")]
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile('videos\\wideo_0.mp4')    