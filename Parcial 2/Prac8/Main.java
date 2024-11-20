public class Main {
    public static void main(String[] args) {
        Auto aut = new Auto("Ford", "Fiesta", 2019);
        Motocicleta mot = new  Motocicleta("Mortalica", "FT150", 2020);
        Camion can = new Camion("Dina", "GT100", 2010);

        aut.encender();
        aut.apagar();
        aut.describir();

        System.out.println();

        mot.encender();
        mot.apagar();
        mot.describir();

        System.out.println();

        can.encender();
        can.apagar();
        can.describir();
    }
}