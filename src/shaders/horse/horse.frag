#version 330 core

in vec3 w_position, w_normal;
in vec2 frag_tex_coords;

uniform vec3 w_camera_position;
uniform sampler2D diffuse_map;

out vec4 out_color;

void main() {
    vec4 texture_color = texture(diffuse_map, frag_tex_coords);
    out_color = texture_color;
}