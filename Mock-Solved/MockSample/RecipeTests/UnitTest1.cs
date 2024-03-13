using Moq;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using RecipeManagementSystem.Models;
using RecipeManagementSystem.Services;

namespace RecipeTests;

public class Tests
{
    // Unit Tests
    private IRecipeService _recipeService;
    
    // Moq
    private IRecipeService _recipeServiceWithLogger;
    private Mock<ActionLogger> _actionLogger;
        
    // Selenium
    private IWebDriver _driver;
    private const string BaseUrl = "https://search.yahoo.com/";
    
    [SetUp]
    public void Setup()
    {
        _recipeService = new RecipeService();
        _actionLogger = new Mock<ActionLogger>();
        _recipeServiceWithLogger = new RecipeService(_actionLogger.Object);
    }

    [Test]
    public void Test1_ViewAllRecipes()
    {
        var result = _recipeService.GetAll();
        Assert.NotNull(result); ;
    }

    [Test]
    public void Test2_ViewOneRecipe()
    {
        var result = _recipeService.GetById(Guid.Parse("b2e6c672-7db8-44bb-806d-1c0dbc9cbb69"));
        Assert.NotNull(result);
    }
    
    [Test]
    public void Test3_AddRecipe()
    {
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Recipe",
            Description = "Recipe description"
        };
        _recipeService.Add(recipe);
        
        Assert.IsTrue(_recipeService.GetAll().Contains(recipe));
    }
    
    [Test]
    public void Test4_EditRecipe()
    {
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Recipe to edit",
            Description = "Recipe description"
        };
        _recipeService.Add(recipe);
        
        var updatedRecipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Updated recipe name",
            Description = "Updated recipe description"
        };
        _recipeService.Update(recipe.Id, updatedRecipe);

        var testUpdatedRecipe = _recipeService.GetById(recipe.Id);
        Assert.That(testUpdatedRecipe.Name, Is.EqualTo(updatedRecipe.Name));
        Assert.That(testUpdatedRecipe.Description, Is.EqualTo(updatedRecipe.Description));
        
        _recipeService.Delete(recipe.Id);
    }

    [Test]
    public void Test5_DeleteARecipe()
    {
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Recipe to delete",
            Description = "Recipe description"
        };
        _recipeService.Add(recipe);
        _recipeService.Delete(recipe.Id);
        Assert.IsNull(_recipeService.GetById(recipe.Id));
    }
    
    [Test]
    public void Test6_SearchByName_LowerCase()
    {
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Find this recipe by Shakalaka",
            Description = "Recipe description"
        };
        _recipeService.Add(recipe);
        var foundRecipe = _recipeService.Search("shakalaka");
        Assert.IsNotNull(foundRecipe);
        
        _recipeService.Delete(recipe.Id);
    }
    
    [Test]
    public void Test7_SearchByName_UpperCase()
    {
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Find this recipe by Shakalaka",
            Description = "Recipe description"
        };
        _recipeService.Add(recipe);
        var foundRecipe = _recipeService.Search("SHAKALAKA");
        Assert.IsNotNull(foundRecipe);
        
        _recipeService.Delete(recipe.Id);
    }
    
    [Test]
    public void Test8_SearchByDescription_LowerCase()
    {
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Find this recipe by Shakalaka",
            Description = "Recipe description by Tukulatu"
        };
        _recipeService.Add(recipe);
        var foundRecipe = _recipeService.Search("tukulatu");
        Assert.IsNotNull(foundRecipe);
        
        _recipeService.Delete(recipe.Id);
    }
    
    [Test]
    public void Test9_SearchByDescription_UpperCase()
    {
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Find this recipe by Shakalaka",
            Description = "Recipe description by Tukulatu"
        };
        _recipeService.Add(recipe);
        var foundRecipe = _recipeService.Search("TUKULATU");
        Assert.IsNotNull(foundRecipe);
        
        _recipeService.Delete(recipe.Id);
    }
    
    [Test]
    public void Test10_SearchNonExistingRecipe()
    {
        var foundRecipe = _recipeService.Search("sasalala");
        Assert.IsEmpty(foundRecipe);
    }
    
    [Test]
    public void Test11_Selenium()
    {
        _driver = new ChromeDriver();
        _driver.Manage().Window.Maximize();
        _driver.Navigate().GoToUrl(BaseUrl);

        _driver.FindElement(By.XPath("//*[@id=\"yschsp\"]")).SendKeys("Wiut");
        _driver.FindElement(By.XPath("//*[@id=\"yschsp\"]")).SendKeys(Keys.Enter);
        
        Thread.Sleep(2000);

        var result = _driver.FindElement(By.CssSelector("#web > ol > li.first > div > div.compTitle.options-toggle > h3 > a")).Text;
        Console.WriteLine(result);
        _driver.Close();
    }

    [Test]
    public void Test12_Moq_Add()
    {
        // Arrange
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Test Recipe",
            Description = "Test Recipe Description"
        };
        
        _recipeServiceWithLogger.Add(recipe);

        _actionLogger.Verify(
            logger => logger.LogActions("Add", recipe.Name),
            Times.Once);
    }

    [Test]
    public void Test12_Moq_Update()
    {
        // Arrange
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Test Recipe",
            Description = "Test Recipe Description"
        };

        var newRecipe = new Recipe()
        {
            Id = recipe.Id,
            Name = "Updated Recipe",
            Description = "Updated Description"
        };

        _recipeServiceWithLogger.Add(recipe);
        _recipeServiceWithLogger.Update(recipe.Id, newRecipe);
        
        _actionLogger.Verify(
            logger => logger.LogActions("Update", recipe.Name),
            Times.Once);
    }

    [Test]
    public void Test12_Moq_Delete()
    {
        // Arrange
        var recipe = new Recipe()
        {
            Id = Guid.NewGuid(),
            Name = "Test Recipe",
            Description = "Test Recipe Description"
        };

        _recipeServiceWithLogger.Add(recipe);
        _recipeServiceWithLogger.Delete(recipe.Id);
        
        _actionLogger.Verify(
            logger => logger.LogActions("Delete", recipe.Name),
            Times.Once);
    }
}