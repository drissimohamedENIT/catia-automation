import win32com.client
import time

class CatiaApp:
    def __init__(self, visible=True, retry=3, retry_delay=1.0):
        self.catia = None
        for i in range(retry):
            try:
                self.catia = win32com.client.Dispatch("CATIA.Application")
                break
            except Exception:
                time.sleep(retry_delay)
        if self.catia is None:
            raise RuntimeError("Impossible de se connecter à CATIA via COM")
        self.catia.Visible = visible

    def new_part(self, name="Part1"):
        documents = self.catia.Documents
        part_doc = documents.Add("Part")
        try:
            part_doc.Name = name
        except Exception:
            pass
        return part_doc
