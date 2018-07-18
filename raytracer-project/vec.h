#ifndef _VEC_H
#define _VEC_H
#include<iostream>
#include<math.h>
using namespace std;

class Vector{
private:
    double x,y,z;
public:
	//Vector():x(0),y(0),z(0){};
    Vector(double a=0, double b=0, double c=0):x(a),y(b),z(c){}; 
    Vector(const Vector& B){
        x=B.x;
        y=B.y;
        z=B.z;
    }
    ~Vector(){};
    friend ostream& operator<<(ostream &wej, Vector A);
    friend istream& operator>>(istream &wej, Vector& M);
    Vector& operator=(const Vector& B){
        x=B.x;
        y=B.y;
        z=B.z;
        return *this;
    }

    Vector operator + (const Vector& B)const{
        return Vector(x+B.x, y+B.y, z+B.z);
    }
    Vector operator - (const Vector& B)const{
        return Vector(x-B.x, y-B.y, z-B.z);
    }
    Vector operator * (double s)const{
        return Vector(x*s,y*s,z*s);
    }
    Vector operator / (double s)const{
        try{
            if (s==0){
                throw 0;
            }
            return Vector(x/s,y/s,z/s);
        }
        catch(int err){
            if (err==0) cout<<"nie dzieli sie przez 0!!!"<<endl;
        }
        
    }
    Vector operator * (const Vector& B)const{
        return Vector(y*B.z-z*B.y, z*B.x - x*B.z, x*B.y-y*B.x);
    }
    double scalar(const Vector& B){
        return x*B.x+y*B.y+z*B.z;
    }
    bool operator == (const Vector& B){
        return x==B.x && y==B.y && z==B.z;
    }
    bool operator != (const Vector& B){
        return !(*this==B);
    }
    double getX(){
    	return x;
    }
     double getY(){
    	return y;
    }
     double getZ(){
    	return z;
    }
    void set_values(double _x, double _y, double _z){
    	x=_x;
    	y=_y;
    	z=_z;
    }
};
Vector operator * (double s, Vector A){
    return A*s;
}
Vector operator - (Vector& A){
    return A*(-1);
}
ostream& operator<<(ostream& wej, Vector A){
        cout<<"wektor: ["<<A.x<<","<<A.y<<","<<A.z<<"]"<<endl;
        return wej;
};
istream& operator>>(istream& wej, Vector& A){
    double x,y,z;
    cout<<"Wprowadz wspolrzedne"<<endl;
        cin>>x>>y>>z;
        A.x=x;
        A.y=y;
        A.z=z;
        return wej;
};
Vector Normalize(Vector A){
	double a = sqrt(A.getX()*A.getX() +A.getY()*A.getY()+A.getZ()*A.getZ());
	Vector N(A.getX()/a, A.getY()/a, A.getZ()/a);
	return N;
}
#endif