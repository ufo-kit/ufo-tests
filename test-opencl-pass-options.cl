#ifndef FOO
#define FOO 0
#endif

kernel void f(global float *x, global float *y)
{
    y[0] = FOO;
}
