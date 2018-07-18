#ifndef _LIGHT_H
#define _LIGHT_H
#include "vec.h"
class Light{
private:
	Vector pos;
	double intensity;
	unsigned char r;
	unsigned char g;
	unsigned char b;
public:
	Light(Vector _pos, double i, unsigned char _r,unsigned char _g, unsigned char _b):pos(_pos), intensity(i),r(_r),g(_g),b(_b){};
	Light(Vector _pos, double i):pos(_pos), intensity(i), r(255),g(255),b(255){};
	Light(Vector _pos):pos(_pos), intensity(1.0),r(255),g(255),b(255){};
	~Light(){};
	Vector& getPos(){
		return pos;
	}
	double getIntensity(){return intensity;}
	unsigned char getR(){return r;}
	unsigned char getG(){return g;}
	unsigned char getB(){return b;}
};	
#endif