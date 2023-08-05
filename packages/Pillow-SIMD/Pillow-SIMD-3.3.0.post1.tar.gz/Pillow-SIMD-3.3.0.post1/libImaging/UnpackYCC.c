/*
 * The Python Imaging Library.
 * $Id$
 *
 * code to convert and unpack PhotoYCC data
 *
 * history:
 * 97-01-25 fl	Moved from PcdDecode.c
 *
 * Copyright (c) Fredrik Lundh 1996-97.
 * Copyright (c) Secret Labs AB 1997.
 *
 * See the README file for information on usage and redistribution.
 */


#include "Imaging.h"


/* Tables generated by pcdtables.py, based on transforms taken from
   the "Colour Space Conversions FAQ" by Roberts/Ford. */

static INT16 L[] = { 0, 1, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15, 16, 18,
19, 20, 22, 23, 24, 26, 27, 29, 30, 31, 33, 34, 35, 37, 38, 39, 41,
42, 43, 45, 46, 48, 49, 50, 52, 53, 54, 56, 57, 58, 60, 61, 62, 64,
65, 67, 68, 69, 71, 72, 73, 75, 76, 77, 79, 80, 82, 83, 84, 86, 87,
88, 90, 91, 92, 94, 95, 96, 98, 99, 101, 102, 103, 105, 106, 107, 109,
110, 111, 113, 114, 115, 117, 118, 120, 121, 122, 124, 125, 126, 128,
129, 130, 132, 133, 134, 136, 137, 139, 140, 141, 143, 144, 145, 147,
148, 149, 151, 152, 153, 155, 156, 158, 159, 160, 162, 163, 164, 166,
167, 168, 170, 171, 173, 174, 175, 177, 178, 179, 181, 182, 183, 185,
186, 187, 189, 190, 192, 193, 194, 196, 197, 198, 200, 201, 202, 204,
205, 206, 208, 209, 211, 212, 213, 215, 216, 217, 219, 220, 221, 223,
224, 225, 227, 228, 230, 231, 232, 234, 235, 236, 238, 239, 240, 242,
243, 245, 246, 247, 249, 250, 251, 253, 254, 255, 257, 258, 259, 261,
262, 264, 265, 266, 268, 269, 270, 272, 273, 274, 276, 277, 278, 280,
281, 283, 284, 285, 287, 288, 289, 291, 292, 293, 295, 296, 297, 299,
300, 302, 303, 304, 306, 307, 308, 310, 311, 312, 314, 315, 317, 318,
319, 321, 322, 323, 325, 326, 327, 329, 330, 331, 333, 334, 336, 337,
338, 340, 341, 342, 344, 345, 346 };

static INT16 CB[] = { -345, -343, -341, -338, -336, -334, -332, -329,
-327, -325, -323, -321, -318, -316, -314, -312, -310, -307, -305,
-303, -301, -298, -296, -294, -292, -290, -287, -285, -283, -281,
-278, -276, -274, -272, -270, -267, -265, -263, -261, -258, -256,
-254, -252, -250, -247, -245, -243, -241, -239, -236, -234, -232,
-230, -227, -225, -223, -221, -219, -216, -214, -212, -210, -207,
-205, -203, -201, -199, -196, -194, -192, -190, -188, -185, -183,
-181, -179, -176, -174, -172, -170, -168, -165, -163, -161, -159,
-156, -154, -152, -150, -148, -145, -143, -141, -139, -137, -134,
-132, -130, -128, -125, -123, -121, -119, -117, -114, -112, -110,
-108, -105, -103, -101, -99, -97, -94, -92, -90, -88, -85, -83, -81,
-79, -77, -74, -72, -70, -68, -66, -63, -61, -59, -57, -54, -52, -50,
-48, -46, -43, -41, -39, -37, -34, -32, -30, -28, -26, -23, -21, -19,
-17, -15, -12, -10, -8, -6, -3, -1, 0, 2, 4, 7, 9, 11, 13, 16, 18, 20,
22, 24, 27, 29, 31, 33, 35, 38, 40, 42, 44, 47, 49, 51, 53, 55, 58,
60, 62, 64, 67, 69, 71, 73, 75, 78, 80, 82, 84, 86, 89, 91, 93, 95,
98, 100, 102, 104, 106, 109, 111, 113, 115, 118, 120, 122, 124, 126,
129, 131, 133, 135, 138, 140, 142, 144, 146, 149, 151, 153, 155, 157,
160, 162, 164, 166, 169, 171, 173, 175, 177, 180, 182, 184, 186, 189,
191, 193, 195, 197, 200, 202, 204, 206, 208, 211, 213, 215, 217, 220 };

static INT16 GB[] = { 67, 67, 66, 66, 65, 65, 65, 64, 64, 63, 63, 62,
62, 62, 61, 61, 60, 60, 59, 59, 59, 58, 58, 57, 57, 56, 56, 56, 55,
55, 54, 54, 53, 53, 52, 52, 52, 51, 51, 50, 50, 49, 49, 49, 48, 48,
47, 47, 46, 46, 46, 45, 45, 44, 44, 43, 43, 43, 42, 42, 41, 41, 40,
40, 40, 39, 39, 38, 38, 37, 37, 37, 36, 36, 35, 35, 34, 34, 34, 33,
33, 32, 32, 31, 31, 31, 30, 30, 29, 29, 28, 28, 28, 27, 27, 26, 26,
25, 25, 25, 24, 24, 23, 23, 22, 22, 22, 21, 21, 20, 20, 19, 19, 19,
18, 18, 17, 17, 16, 16, 15, 15, 15, 14, 14, 13, 13, 12, 12, 12, 11,
11, 10, 10, 9, 9, 9, 8, 8, 7, 7, 6, 6, 6, 5, 5, 4, 4, 3, 3, 3, 2, 2,
1, 1, 0, 0, 0, 0, 0, -1, -1, -2, -2, -2, -3, -3, -4, -4, -5, -5, -5,
-6, -6, -7, -7, -8, -8, -8, -9, -9, -10, -10, -11, -11, -11, -12, -12,
-13, -13, -14, -14, -14, -15, -15, -16, -16, -17, -17, -18, -18, -18,
-19, -19, -20, -20, -21, -21, -21, -22, -22, -23, -23, -24, -24, -24,
-25, -25, -26, -26, -27, -27, -27, -28, -28, -29, -29, -30, -30, -30,
-31, -31, -32, -32, -33, -33, -33, -34, -34, -35, -35, -36, -36, -36,
-37, -37, -38, -38, -39, -39, -39, -40, -40, -41, -41, -42 };

static INT16 CR[] = { -249, -247, -245, -243, -241, -239, -238, -236,
-234, -232, -230, -229, -227, -225, -223, -221, -219, -218, -216,
-214, -212, -210, -208, -207, -205, -203, -201, -199, -198, -196,
-194, -192, -190, -188, -187, -185, -183, -181, -179, -178, -176,
-174, -172, -170, -168, -167, -165, -163, -161, -159, -157, -156,
-154, -152, -150, -148, -147, -145, -143, -141, -139, -137, -136,
-134, -132, -130, -128, -127, -125, -123, -121, -119, -117, -116,
-114, -112, -110, -108, -106, -105, -103, -101, -99, -97, -96, -94,
-92, -90, -88, -86, -85, -83, -81, -79, -77, -76, -74, -72, -70, -68,
-66, -65, -63, -61, -59, -57, -55, -54, -52, -50, -48, -46, -45, -43,
-41, -39, -37, -35, -34, -32, -30, -28, -26, -25, -23, -21, -19, -17,
-15, -14, -12, -10, -8, -6, -4, -3, -1, 0, 2, 4, 5, 7, 9, 11, 13, 15,
16, 18, 20, 22, 24, 26, 27, 29, 31, 33, 35, 36, 38, 40, 42, 44, 46,
47, 49, 51, 53, 55, 56, 58, 60, 62, 64, 66, 67, 69, 71, 73, 75, 77,
78, 80, 82, 84, 86, 87, 89, 91, 93, 95, 97, 98, 100, 102, 104, 106,
107, 109, 111, 113, 115, 117, 118, 120, 122, 124, 126, 128, 129, 131,
133, 135, 137, 138, 140, 142, 144, 146, 148, 149, 151, 153, 155, 157,
158, 160, 162, 164, 166, 168, 169, 171, 173, 175, 177, 179, 180, 182,
184, 186, 188, 189, 191, 193, 195, 197, 199, 200, 202, 204, 206, 208,
209, 211, 213, 215 };

static INT16 GR[] = { 127, 126, 125, 124, 123, 122, 121, 121, 120, 119,
118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 108, 107, 106,
105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 95, 95, 94, 93, 92, 91,
90, 89, 88, 87, 86, 85, 84, 83, 83, 82, 81, 80, 79, 78, 77, 76, 75,
74, 73, 72, 71, 70, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59,
58, 57, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 45, 44,
43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 32, 31, 30, 29, 28,
27, 26, 25, 24, 23, 22, 21, 20, 19, 19, 18, 17, 16, 15, 14, 13, 12,
11, 10, 9, 8, 7, 6, 6, 5, 4, 3, 2, 1, 0, 0, -1, -2, -3, -4, -5, -5,
-6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -18, -19,
-20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -31, -32,
-33, -34, -35, -36, -37, -38, -39, -40, -41, -42, -43, -44, -44, -45,
-46, -47, -48, -49, -50, -51, -52, -53, -54, -55, -56, -56, -57, -58,
-59, -60, -61, -62, -63, -64, -65, -66, -67, -68, -69, -69, -70, -71,
-72, -73, -74, -75, -76, -77, -78, -79, -80, -81, -82, -82, -83, -84,
-85, -86, -87, -88, -89, -90, -91, -92, -93, -94, -94, -95, -96, -97,
-98, -99, -100, -101, -102, -103, -104, -105, -106, -107, -107, -108 };

#define	R 0
#define	G 1
#define	B 2
#define	A 3

#define	YCC2RGB(rgb, y, cb, cr) {\
    int l = L[y];\
    int r = l + CR[cr];\
    int g = l + GR[cr] + GB[cb];\
    int b = l + CB[cb];\
    rgb[0] = (r <= 0) ? 0 : (r >= 255) ? 255 : r;\
    rgb[1] = (g <= 0) ? 0 : (g >= 255) ? 255 : g;\
    rgb[2] = (b <= 0) ? 0 : (b >= 255) ? 255 : b;\
}

void
ImagingUnpackYCC(UINT8* out, const UINT8* in, int pixels)
{
    int i;
    /* PhotoYCC triplets */
    for (i = 0; i < pixels; i++) {
	YCC2RGB(out, in[0], in[1], in[2]);
	out[A] = 255;
	out += 4; in += 3;
    }
}

void
ImagingUnpackYCCA(UINT8* out, const UINT8* in, int pixels)
{
    int i;
    /* PhotoYCC triplets plus premultiplied alpha */
    for (i = 0; i < pixels; i++) {
	/* Divide by alpha */
	UINT8 rgb[3];
	rgb[0] = (in[3] == 0) ? 0 : (((int) in[0] * 255) / in[3]);
	rgb[1] = (in[3] == 0) ? 0 : (((int) in[1] * 255) / in[3]);
	rgb[2] = (in[3] == 0) ? 0 : (((int) in[2] * 255) / in[3]);
	/* Convert non-multiplied data to RGB */
	YCC2RGB(out, rgb[0], rgb[1], rgb[2]);
	out[A] = in[3];
	out += 4; in += 4;
    }
}
