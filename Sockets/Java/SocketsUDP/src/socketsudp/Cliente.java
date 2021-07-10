/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package socketsudp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

/**
 *
 * @author Ricardo Alberto
 */
public class Cliente {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
  
        final int PUERTO_SERVIDOR=5000;
        byte[] buffer=new byte[1024]; //Buffer para el datagrama
        try{
        InetAddress direccionServidor=InetAddress.getByName("localhost");
        
        //Un socket de datagrama es el
        //del cleinte si no tiene el puerto
        //el mismo código lo asigna el puerto del cliente
        DatagramSocket socketUDP=new DatagramSocket();
        
        String mensaje ="!Hola mundo desde el cleinte";
        
        buffer=mensaje.getBytes();
        DatagramPacket pregunta=new DatagramPacket(buffer, buffer.length,direccionServidor,PUERTO_SERVIDOR);
            System.out.println("Envio el datagrama");
        socketUDP.send(pregunta);
        
        DatagramPacket peticion=new DatagramPacket(buffer,buffer.length);
        
        socketUDP.receive(peticion);
 
            System.out.println("Recibo lapetición");
        
        mensaje=new String(peticion.getData());
        System.out.println(mensaje);
        socketUDP.close();
        
        }catch(Exception ex){
        
        }
        
    }
    
}
