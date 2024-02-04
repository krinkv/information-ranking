import {Component, OnInit} from '@angular/core';
import {DocumentRetrievingService} from "../../services/document-retrieving.service";

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrl: './search.component.css'
})
export class SearchComponent {
  inputValue: string = '';


  constructor(private documentRetrievingService: DocumentRetrievingService) {
  }

  onSubmit() {
    this.documentRetrievingService.getBestDocumentCandidates(this.inputValue);
  }

  /**
   * The purpose of this event is to check if the user has finished the word he was currently writing
   * We send the word to the spellchecker and the aim is to provide 3 best suggestions if the word is misspelled
   * @param event
   */
  onInputChange(event: Event): void {
    // This method is called on each change in the input field
    this.inputValue = (event.target as HTMLInputElement).value;
    console.log('Input Value:', this.inputValue);
  }
}
