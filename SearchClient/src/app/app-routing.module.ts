import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SearchComponent } from "./components/search/search.component";
import { SearchResultComponent } from "./components/search-result/search-result.component";
import {PresentDocumentComponent} from "./components/present-document/present-document.component";

const routes: Routes = [
  {
    path: 'search', component: SearchComponent
  },
  {
    path: 'search-result', component: SearchResultComponent
  },
  {
    path: 'document/:id', component: PresentDocumentComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
