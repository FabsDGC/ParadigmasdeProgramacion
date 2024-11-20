public class Auto extends  Vehiculo{

    public Auto(String marca, String modelo, int anio){
        this.marca = marca;
        this.modelo = modelo;
        this.anio = anio;
    }

    @Override
    public void encender() {
        super.encender();
        System.out.println("El auto se ha encendido");
    }

    @Override
    public void apagar() {
        super.apagar();
        System.out.println("El auto se ha apagado");
    }

    @Override
    public void describir() {
        super.describir();
        System.out.println("Marca del auto: " + marca);
        System.out.println("Modelo del auto: " + modelo);
        System.out.printf("Anio del auto: " +  anio);
    }
}