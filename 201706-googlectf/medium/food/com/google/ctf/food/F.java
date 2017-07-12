package com.google.ctf.food;

public class F {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		byte[] flag=new byte[]{(byte) -19, (byte) 116, (byte) 58, (byte) 108, (byte) -1, (byte) 33, (byte) 9, (byte) 61, (byte) -61, (byte) -37, (byte) 108, (byte) -123, (byte) 3, (byte) 35, (byte) 97, (byte) -10, (byte) -15, (byte) 15, (byte) -85, (byte) -66, (byte) -31, (byte) -65, (byte) 17, (byte) 79, (byte) 31, (byte) 25, (byte) -39, (byte) 95, (byte) 93, (byte) 1, (byte) -110, (byte) -103, (byte) -118, (byte) -38, (byte) -57, (byte) -58, (byte) -51, (byte) -79};
		byte[] k=new byte[]{(byte)9,(byte) 10, (byte)13, (byte)7,(byte) 17, (byte)1, (byte)19, (byte)2};
		byte[] result=R.C(flag, k);
		System.out.println(new String(result));
	}
}
