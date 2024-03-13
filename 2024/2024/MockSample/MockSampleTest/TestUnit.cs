using RecipeManagementSystem.Models;
using RecipeManagementSystem.Services;

namespace MockSampleTest;

[TestClass]
public class TestUnit
{
    private RecipeService recipeService;

    [TestInitialize]
    public void TestInitialize()
    {
        recipeService = new RecipeService();
    }

    [TestMethod]
    public void TestRecipeCreateEmptyName()
    {
        Recipe recipe = new Recipe();
        recipe.Name = "";
        recipe.Description = "Value";

        recipeService.Add(recipe);
        Recipe createdRecipe = recipeService.GetById(recipe.Id);

        Assert.IsNull(createdRecipe);
        Assert.ThrowsException<Exception>(() => recipeService.Add(recipe));
    }

    [TestMethod]
    public void TestRecipeCreateEmptyDescription()
    {
        Recipe recipe = new Recipe();
        recipe.Name = "Value";
        recipe.Description = "";

        recipeService.Add(recipe);
        Recipe createdRecipe = recipeService.GetById(recipe.Id);

        Assert.IsNull(createdRecipe);
        Assert.ThrowsException<Exception>(() => recipeService.Add(recipe));
    }

    [TestMethod]
    public void TestRecipeCreateValidData()
    {
        Recipe recipe = new Recipe();
        recipe.Name = "Recipe1";
        recipe.Description = "Recipe Info";

        recipeService.Add(recipe);
        Recipe createdRecipe = recipeService.GetById(recipe.Id);

        Assert.IsNotNull(createdRecipe);
        Assert.AreEqual(recipe.Id, createdRecipe.Id);
    }

    [TestMethod]
    public void TestUpdateNotExistingRecipe()
    {
        Recipe recipe = new Recipe();
        recipe.Name = "Recipe (Updated)";
        recipe.Description = "Recipe Info (Updated)";
        Guid notExistingRecipeId = Guid.NewGuid();

        Assert.ThrowsException<Exception>(() => recipeService.Update(notExistingRecipeId, recipe));
    }

    [TestMethod]
    public void TestUpdateExistingRecipe()
    {
        Recipe recipe = new Recipe();
        recipe.Name = "Recipe (Updated)";
        recipe.Description = "Recipe Info (Updated)";

        Guid lastRecipeId = recipeService.GetAll().Last().Id;
        recipeService.Update(lastRecipeId, recipe);
        Recipe lastRecipe = recipeService.GetAll().Last();

        Assert.AreEqual(lastRecipe.Name, recipe.Name);
        Assert.AreEqual(lastRecipe.Description, recipe.Description);
    }

    [TestMethod]
    public void TestSearchByNotMatchingName()
    {
        string notMatchingName = "Not matching name";
        List<Recipe> recipes = recipeService.Search(notMatchingName);
        Assert.AreEqual(recipes.Count(), 0);
    }

    [TestMethod]
    public void TestSearchByMatchingName()
    {
        string matchingName = "Recipe1";
        List<Recipe> recipes = recipeService.Search(matchingName);
        Assert.AreNotEqual(recipes.Count(), 0);
    }

    [TestMethod]
    public void TestSearchByNotMatchingDescription()
    {
        string notMatchingDescription = "Not matching description";
        List<Recipe> recipes = recipeService.Search(notMatchingDescription);
        Assert.AreEqual(recipes.Count(), 0);
    }

    [TestMethod]
    public void TestSearchByMatchingDescription()
    {
        string matchingDescription = "Recipe Info";
        List<Recipe> recipes = recipeService.Search(matchingDescription);
        Assert.AreNotEqual(recipes.Count(), 0);
    }

    [TestMethod]
    public void TestRetrieveRecipeExistingId()
    {
        Recipe firstRecipe = recipeService.GetAll().First();
        Recipe recipe = recipeService.GetById(firstRecipe.Id);
        Assert.AreEqual(recipe.Name, firstRecipe.Name);
        Assert.AreEqual(recipe.Description, firstRecipe.Description);
    }
}
