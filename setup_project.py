import os

# Határozzuk meg a létrehozandó struktúrát
# A szótár kulcsai a mappák, a listák elemei pedig a fájlok abban a mappában
structure = {
    ".": [
        ".env.example",
        "Dockerfile",
        "docker-compose.yml",
        "requirements.txt",
        "README.md",
    ],
    "app": ["main.py"],
    "app/core": ["config.py", "logging.py", "dependencies.py"],
    "app/api/routes": ["health.py", "agent.py", "eval.py"],
    "app/schemas": ["request.py", "response.py", "eval.py"],
    "app/services": [
        "agent_service.py",
        "prompt_service.py",
        "evaluation_service.py",
    ],
    "app/graph": ["builder.py", "state.py"],
    "app/graph/nodes": ["planner.py", "researcher.py", "writer.py", "reviewer.py"],
    "app/graph/tools": ["web_search.py", "calculator.py"],
    "app/utils": ["formatters.py"],
    "tests": ["test_health.py", "test_agent_api.py", "test_graph_flow.py"],
    "scripts": ["run_demo.sh"],
}


def create_project_structure():
    print("🚀 Projekt szerkezet létrehozásának indítása...")

    current_dir = os.getcwd()
    print(f"📍 Aktuális mappa: {current_dir}")

    for folder, files in structure.items():
        # Mappa létrehozása (ha nem a gyökérkönyvtár '.')
        if folder != ".":
            os.makedirs(folder, exist_ok=True)
            print(f"📁 Mappa létrehozva: {folder}")

            # Python specifikus: minden almappába teszünk egy üres __init__.py-t,
            # hogy a Python modulként kezelje őket és működjenek az importok
            init_file = os.path.join(folder, "__init__.py")
            if not os.path.exists(init_file):
                with open(init_file, "w", encoding="utf-8") as f:
                    pass

        # Fájlok létrehozása az adott mappában
        for file in files:
            file_path = os.path.join(folder, file) if folder != "." else file
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    # Opcionálisan tehetünk egy alap megjegyzést a Python fájlokba
                    if file.endswith(".py"):
                        f.write(f'# {file} - Kezdeti fájl\n')
                print(f"  📄 Fájl létrehozva: {file_path}")
            else:
                print(f"  ⚠️ Fájl már létezik, átugorva: {file_path}")

    print("\n✅ A projekt struktúra sikeresen elkészült!")


if __name__ == "__main__":
    create_project_structure()
