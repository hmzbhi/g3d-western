#version 330 core

in vec3 w_position, w_normal;
in vec2 frag_tex_coords;

uniform vec3 light_dir;
uniform vec3 k_d, k_a, k_s;
uniform float s;
uniform vec3 w_camera_position;
uniform sampler2D diffuse_map;

out vec4 out_color;

void main() {
    vec3 n = normalize(w_normal);
    vec3 l = normalize(-light_dir);
    vec3 r = reflect(-l, n);
    vec3 v = normalize(w_camera_position - w_position);

    vec3 diffuse_color = k_d * max(dot(n, l), 0.0);
    vec3 specular_color = k_s * pow(max(dot(r, v), 0.0), s);

    vec4 illumination_color = vec4(k_a, 1) + vec4(diffuse_color, 1) + vec4(specular_color, 1);
    vec4 texture_color = texture(diffuse_map, frag_tex_coords);

    out_color = mix(illumination_color, texture_color, 0.5);
}