
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Ricardo Alberto
 */
public class Servidor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       
       
        ServerSocket servidor=null;
        Socket sc=null;
        //El puerto debe ser uno muy alto para asi poder asegurar que esta libre entre uno y 65000
        final int PUERTO=5000; 
        DataInputStream in;
        DataOutputStream out;

        try{ 
        servidor=new ServerSocket(PUERTO); //Creacion de elemento de servidor del socketr
        System.out.println("Servidro iniciado");
        
        while(true){
        
          sc=servidor.accept();//Método que espera una petición dle cliente
          //Stream de datos que recibe el servidor del socket del cliente
          in=new DataInputStream(sc.getInputStream());
          //Stream de datos que sca el servidor al socket dle cliente
          out=new DataOutputStream(sc.getOutputStream());
          
          
          String mensaje=in.readUTF();
          
        }
        
        
        
        }catch(IOException ex){
           
        }
        
        
    }
    
}
