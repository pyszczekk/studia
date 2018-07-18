#ifndef _SPHERE_H
#define _SPHERE_H
#include "vec.h"
#include "ray.h"
#include <math.h>
#include "obj.h"
bool solveQuadratic(const double &a, const double &b, const double &c, double &x0, double &x1) 
{ 
    double discr = b * b - 4 * a * c; 
    if (discr < 0) return false; 
    else if (discr == 0) x0 = x1 = - 0.5 * b / a; 
    else { 
        double q = (b > 0) ? 
           	-0.5 * (b + sqrt(discr)) : 
            -0.5 * (b - sqrt(discr)); 
        x0 = q / a; 
        x1 = c / q; 
    } 
    if (x0 > x1) std::swap(x0, x1); 
 
    return true; 
} 
class Sphere:public Obj{
private:
	Vector c; // center
	double r; // radius
	unsigned char rc;
	unsigned char gc;
	unsigned char bc;
	bool phong;

public:
	Sphere(Vector _c, double _r, unsigned char _rc, unsigned char _gc, unsigned char _bc, bool x):c(_c),r(_r*(1+(-1)*_c.getZ()/100)), rc(_rc), gc(_gc),bc(_bc), phong(x){};
	~Sphere(){};
	bool cross(Ray& ray, double &t){
		Vector o = ray.getOrigin();
		Vector d = ray.getDirection();
		double t0,t1;
		if(t==0){
			Vector L =c-o;
			double tca = L.scalar(d);
			double d2 =L.scalar(L)-tca*tca;
			if(d2 > r*r)return false;
			double thc =sqrt(r*r-d2);
			t0=tca-thc;
			t1=tca+thc;
		}else{
			Vector L = o-c;
			double a = d.scalar(d);
			double b =2*d.scalar(L);
			double c = L.scalar(L)-r*r;
			if(!solveQuadratic(a, b, c, t0, t1)) return false;
		}
		if(t0>t1)std::swap(t0,t1);
		if(t0<t1){
			 t0 = t1;
	         if (t0 < 0) return false;
		}
		t=t0;
		return true;
	}
	Vector getNormal(Vector& p){
		Vector x = (c-p)/r;
		return x;
	}
	//Vector& getC(){return c;}
	unsigned char getR(){return rc;}
	unsigned char getG(){return gc;}
	unsigned char getB(){return bc;}
	bool Phong(){return phong;}
};

#endif