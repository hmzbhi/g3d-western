#version 330 core

in vec3 position;
in vec3 normal;
in vec3 tex_coord;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec2 frag_tex_coords;
out vec3 w_position, w_normal;

void main() {
    vec4 w_position4 = model * vec4(position, 1.0);
    gl_Position = projection * view * w_position4;

    w_position = w_position4.xyz / w_position4.w;

    mat3 nit_matrix = transpose(inverse(mat3(model)));
    w_normal = normalize(nit_matrix * normal);

    frag_tex_coords = tex_coord.xy;
}