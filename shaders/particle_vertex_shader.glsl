#version 330 core
layout(location = 0) in vec2 position;
uniform vec2 offset;  // Particle position offset
void main() {
    gl_Position = vec4(position + offset, 0.0, 1.0);
}