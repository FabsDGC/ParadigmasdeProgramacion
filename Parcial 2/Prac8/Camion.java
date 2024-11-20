public class Camion extends Vehiculo{

    public Camion(String marca, String modelo, int anio){
        this.marca = marca;
        this.modelo = modelo;
        this.anio = anio;
    }

    @Override
    public void encender() {
        super.encender();
        System.out.println("El camion ha encendido");
    }

    @Override
    public void apagar() {
        super.apagar();
        System.out.println("El camion se ha apagado");
    }

    @Override
    public void describir() {
        super.describir();
        System.out.println("La marca del camion es: " + marca);
        System.out.println("El modelo del camion es: " + modelo);
        System.out.println("El anio del camion es: " + anio);
    }
}