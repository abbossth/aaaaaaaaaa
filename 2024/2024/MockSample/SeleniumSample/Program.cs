// See https://aka.ms/new-console-template for more information


using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

public class Program
{
    public static void Main(string[] args)
    {
        ChromeDriver chromeDriver = new ChromeDriver();
        chromeDriver.Navigate().GoToUrl("https://search.yahoo.com/");

        string inputXPath = "/html/body/div[1]/div/div[4]/div[3]/div[2]/div[1]/form/div[1]/input";
        string aTagXPath = "/html/body/div[1]/div[3]/div/div/div[1]/div/div/div/div/ol/li[1]/div/div[1]/h3/a";

        IWebElement inputElement = chromeDriver.FindElement(By.XPath(inputXPath));
        inputElement.SendKeys("WIUT");
        inputElement.SendKeys(Keys.Enter);

        IWebElement aTag = chromeDriver.FindElement(By.XPath(aTagXPath));

        Console.WriteLine(aTag.Text);
        Console.ReadLine();
    }
}
