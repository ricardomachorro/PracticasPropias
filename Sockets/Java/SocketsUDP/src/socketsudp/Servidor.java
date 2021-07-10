/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package socketsudp;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;

/**
 *
 * @author Ricardo Alberto
 */
public class Servidor {

    /**
     * @param args the command line arguments
     */
    
    /*
    
    Los socket de datagramas usan normalmente UDP
    esto quiere decir que no hay conexión entre
    cleinte y servidor
    
    No hay handshaking
    
    El emisor debe indicar explícitamente la 
    direcci+on IP  yel puerto del destino para
    cada paquete
    
    Los paquetes pueden mandarse de manera aleatoria
    y los paquetes se puedne perder
    */
    
    
    public static void main(String[] args) {
        // TODO code application logic here
        final int PUERTO=5000;
        byte[] buffer=new byte[1024]; //Buffer para el datagrama
        try{
            //Un socket de datagrama es el
            //del servidor si tiene el puerto
           DatagramSocket socketUDP=new DatagramSocket(PUERTO);
           DatagramPacket peticion=new DatagramPacket(buffer,buffer.length);//Paquete de datagramas a enviar
           socketUDP.receive(peticion);
            System.out.println("Recibe la infromación del cliente");
           String mensaje=new String(peticion.getData());
           System.out.println(mensaje);
           
           int puertoCliente=peticion.getPort();
           InetAddress direccion=peticion.getAddress();
           
           mensaje="Hola mundo desde el servidor";
           buffer=mensaje.getBytes();
           
           DatagramPacket respuesta=new DatagramPacket(buffer,buffer.length,direccion,puertoCliente);
            System.out.println("Enviando la información del cliente");
           socketUDP.send(respuesta);
           
           
           
        }catch(IOException ex){
        System.out.println(ex.toString());
        }
    
    
    }
    
}
