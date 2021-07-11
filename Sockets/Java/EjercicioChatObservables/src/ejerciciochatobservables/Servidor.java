/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ejerciciochatobservables;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.net.ServerSocket;
import java.net.Socket;

import java.util.Observable;

/**
 *
 * @author Ricardo Alberto
 */
public class Servidor extends Observable implements Runnable {

    

    @Override
    public void run() {
        
       ServerSocket socket=null;
       Socket sc=null;
       final int PUERTO=5000;
       DataInputStream in=null;
       DataOutputStream out=null;

       
    }
    
}
