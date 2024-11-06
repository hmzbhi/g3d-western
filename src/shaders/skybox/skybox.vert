#version 330 core

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

in vec3 position;

out vec3 frag_tex_coords;

void main() {
    mat4 view2 = mat4(mat3(view));
    view2[3][3]= 1;
    vec4 pos = projection * view2 * model * vec4(position, 1);
    gl_Position = pos.xyww;
    gl_Position.z -= 0.0001;
    frag_tex_coords = position;
}