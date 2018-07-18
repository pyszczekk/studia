#ifndef _RAY_H
#define _RAY_H
#include <iostream>
#include "vec.h"
class Ray{
private:
	Vector origin; // origin
	Vector dir; //direction
public:
	Ray(Vector a, Vector b):origin(a),dir(b){};
	~Ray(){};
	Vector& getOrigin(){
		return origin;
	}
	Vector& getDirection(){
		return dir;
	}
};
#endif