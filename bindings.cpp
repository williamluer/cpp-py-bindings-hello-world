#include <pybind11/pybind11.h>
#include "Rectangle.h"

namespace py = pybind11;

PYBIND11_MODULE(rectangle, m) {
    m.doc() = "Python bindings for calculating the area of a rectangle using C++";
    m.def("calculate_area", &calculate_area, "Calculate the area of a rectangle");
}
