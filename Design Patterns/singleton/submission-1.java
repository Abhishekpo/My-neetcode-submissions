static class Singleton {
    // this is used many used in state management tools like Redux (react)
    // because at one time we can't have many instance of one state.
    // this is not the part of the Singleton object because this needs to be 
    // belongs to the Singleton class this need to exist before creating an object.
    private static Singleton uniqueInstance = null;

    private String value = null;


    private Singleton() {

    }

    public static Singleton getInstance() {

        if (uniqueInstance == null){
            uniqueInstance = new Singleton();
        }
        return uniqueInstance;
    }

    public String getValue() {
        return this.value;
    }

    public void setValue(String value) {
        this.value=value;

    }
    
}
