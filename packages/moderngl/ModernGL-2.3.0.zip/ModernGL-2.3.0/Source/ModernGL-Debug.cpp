#include "ModernGL.hpp"

#include "OpenGL.hpp"

PyObject * DebugInfo(PyObject * self) {
	PyObject * viewport = PyDict_New();
	PyDict_SetItemString(viewport, "width", PyLong_FromLong(activeViewportWidth));
	PyDict_SetItemString(viewport, "height", PyLong_FromLong(activeViewportHeight));

	PyObject * dict = PyDict_New();
	PyDict_SetItemString(dict, "versionNumber", PyLong_FromLong(versionNumber));
	PyDict_SetItemString(dict, "maxTextureUnits", PyLong_FromLong(maxTextureUnits));
	PyDict_SetItemString(dict, "defaultFramebuffer", PyLong_FromLong(defaultFramebuffer));
	PyDict_SetItemString(dict, "defaultVertexArray", PyLong_FromLong(defaultVertexArray));
	PyDict_SetItemString(dict, "activeFramebuffer", PyLong_FromLong(activeFramebuffer));
	PyDict_SetItemString(dict, "activeProgram", PyLong_FromLong(activeProgram));
	PyDict_SetItemString(dict, "activeViewport", viewport);

	PyObject * textures = PyList_New(maxTextureUnits);

	for (int i = 0; i < maxTextureUnits; ++i) {
		int binding = 0;
		OpenGL::glActiveTexture(OpenGL::GL_TEXTURE0 + i);
		OpenGL::glGetIntegerv(OpenGL::GL_TEXTURE_BINDING_2D, &binding);
		PyList_SET_ITEM(textures, i, PyLong_FromLong(binding));
	}

	PyDict_SetItemString(dict, "textures", textures);
	return dict;
}

PyObject * DebugVar(PyObject * self, PyObject * args) {
	PyObject * obj;

	if (!PyArg_ParseTuple(args, "O:DebugVar", &obj)) {
		return 0;
	}

	if (PyObject_TypeCheck(obj, &FramebufferType)) {
		return PyUnicode_FromString("Framebuffer");
	}

	if (PyObject_TypeCheck(obj, &VertexArrayType)) {
		return PyUnicode_FromString("VertexArray");
	}

	if (PyObject_TypeCheck(obj, &VertexBufferType)) {
		return PyUnicode_FromString("VertexBuffer");
	}

	if (PyObject_TypeCheck(obj, &IndexBufferType)) {
		return PyUnicode_FromString("IndexBuffer");
	}

	if (PyObject_TypeCheck(obj, &UniformBufferType)) {
		return PyUnicode_FromString("UniformBuffer");
	}

	if (PyObject_TypeCheck(obj, &StorageBufferType)) {
		return PyUnicode_FromString("StorageBuffer");
	}

	if (PyObject_TypeCheck(obj, &TextureType)) {
		return PyUnicode_FromString("Texture");
	}

	if (PyObject_TypeCheck(obj, &ShaderType)) {
		return PyUnicode_FromString("Shader");
	}

	if (PyObject_TypeCheck(obj, &ProgramType)) {
		return PyUnicode_FromString("Program");
	}

	if (PyObject_TypeCheck(obj, &UniformLocationType)) {
		return PyUnicode_FromString("UniformLocation");
	}

	if (PyObject_TypeCheck(obj, &UniformBufferLocationType)) {
		return PyUnicode_FromString("UniformBufferLocation");
	}

	if (PyObject_TypeCheck(obj, &ComputeShaderType)) {
		return PyUnicode_FromString("ComputeShader");
	}

	if (PyObject_TypeCheck(obj, &EnableFlagType)) {
		return PyUnicode_FromString("EnableFlag");
	}

	PyErr_Format(ModuleError, "Type %s is not part of ModernGL", GET_OBJECT_TYPENAME(obj));
	return 0;
}
