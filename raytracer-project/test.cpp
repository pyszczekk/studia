#include <iostream>
#include <stdlib.h>
#include "readFile.h"

int main(){
	const uint16_t imgWidth = 500;
	const uint16_t imgHeight = 500;
	JiMP2::BMP bmp(imgWidth, imgHeight);
	bmp.setBackground(); 
	readFile("rayFile.txt", bmp, imgWidth,imgHeight, "test.bmp" );
	return 0;
};