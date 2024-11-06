#version 330 core

uniform vec3 global_color;
uniform float alpha;

out vec4 out_color;

void main() {
    out_color = vec4(global_color, alpha);
}