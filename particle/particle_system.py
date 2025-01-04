from particle.particle import Particle
 
from OpenGL.GL import glUseProgram, glBindVertexArray, glUniform4fv, glGetUniformLocation, glDrawArrays, GL_POINTS


class ParticleSystem:
    def __init__(self, max_particles=1000):
        self.particles = []
        self.max_particles = max_particles

    def emit_particle(self, position, velocity, color, size, lifespan):
        if len(self.particles) < self.max_particles:
            particle = Particle(position, velocity, color, size, lifespan)
            self.particles.append(particle)

    def update(self, delta_time):
        # Update each particle
        for particle in self.particles[:]:
            particle.update(delta_time)
            if not particle.is_alive():
                self.particles.remove(particle)
    
    def draw(self, shader_program, VAO):
        # Draw each particle (you could use points or textured quads)
        glUseProgram(shader_program)
        glBindVertexArray(VAO)

        for particle in self.particles:
            # Here we can pass particle data to the shader for rendering
            # For simplicity, we'll assume the position and color are being updated per particle
            glUniform4fv(glGetUniformLocation(shader_program, "color"), 1, particle.color)
            # Send position (and size if needed) as uniforms or vertex attributes
            # e.g., rendering as points or quads
            glDrawArrays(GL_POINTS, 0, 1)  # Draw each particle as a point

        glBindVertexArray(0)
