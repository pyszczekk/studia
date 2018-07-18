#ifndef _OBJ_H
#define _OBJ_H
#include "vec.h"
#include "ray.h"
class Obj{
private:

public:
	Obj(){};
	virtual ~Obj(){};
	virtual bool cross(Ray& ray, double &t)=0;
	virtual Vector getNormal(Vector& p){return Vector(0,0,1);}
	virtual unsigned char getR(){return 0;};
	virtual unsigned char getG(){return 0;};
	virtual unsigned char getB(){return 0;};
	virtual bool Phong(){return false;}
};

#endif