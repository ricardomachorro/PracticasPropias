/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package socketsudp;

import java.net.DatagramSocket;
import java.net.SocketException;

/**
 *
 * @author Ricardo Alberto
 */
public class Servidor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        final int PUERTO=5000;
        byte[] buffer=new byte[1024];
        try{
           DatagramSocket socketUDP=new DatagramSocket(PUERTO);
        }catch(SocketException ex){
        System.out.println(ex.toString());
        }
    
    
    }
    
}
